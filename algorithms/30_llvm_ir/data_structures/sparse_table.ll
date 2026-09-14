; ModuleID = 'algorithms/02_c/data_structures/sparse_table.c'
source_filename = "algorithms/02_c/data_structures/sparse_table.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@st = internal unnamed_addr global [17 x [100000 x i32]] zeroinitializer, align 16
@lg = internal unnamed_addr global [100001 x i32] zeroinitializer, align 16
@__const.main.a = private unnamed_addr constant [7 x i32] [i32 5, i32 2, i32 4, i32 7, i32 1, i32 8, i32 3], align 16
@str = private unnamed_addr constant [50 x i8] c"[C SparseTable] O(1) range minimum query verified\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local void @sparse_build(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp sgt i32 %1, 0
  br i1 %3, label %4, label %57

4:                                                ; preds = %2
  %5 = zext nneg i32 %1 to i64
  %6 = shl nuw nsw i64 %5, 2
  tail call void @llvm.memcpy.p0.p0.i64(ptr nonnull align 16 @st, ptr align 4 %0, i64 %6, i1 false), !tbaa !5
  %7 = icmp eq i32 %1, 1
  br i1 %7, label %57, label %8

8:                                                ; preds = %4, %66
  %9 = phi i64 [ %67, %66 ], [ 1, %4 ]
  %10 = phi i32 [ %69, %66 ], [ 2, %4 ]
  %11 = add nsw i64 %9, -1
  %12 = getelementptr inbounds [100000 x i32], ptr @st, i64 %11
  %13 = trunc nuw nsw i64 %11 to i32
  %14 = shl nuw i32 1, %13
  %15 = getelementptr inbounds nuw [100000 x i32], ptr @st, i64 %9
  %16 = sext i32 %14 to i64
  %17 = tail call i32 @llvm.smax.i32(i32 %10, i32 %1)
  %18 = add nuw i32 %17, 1
  %19 = sub i32 %18, %10
  %20 = zext i32 %19 to i64
  %21 = getelementptr i32, ptr %12, i64 %16
  %22 = icmp ult i32 %19, 4
  br i1 %22, label %41, label %23

23:                                               ; preds = %8
  %24 = shl nsw i64 %16, 2
  %25 = add nsw i64 %24, -399985
  %26 = icmp ult i64 %25, 16
  br i1 %26, label %41, label %27

27:                                               ; preds = %23
  %28 = and i64 %20, 4294967292
  br label %29

29:                                               ; preds = %29, %27
  %30 = phi i64 [ 0, %27 ], [ %37, %29 ]
  %31 = getelementptr inbounds nuw i32, ptr %12, i64 %30
  %32 = load <4 x i32>, ptr %31, align 16, !tbaa !5
  %33 = getelementptr i32, ptr %21, i64 %30
  %34 = load <4 x i32>, ptr %33, align 4, !tbaa !5
  %35 = tail call <4 x i32> @llvm.smin.v4i32(<4 x i32> %32, <4 x i32> %34)
  %36 = getelementptr inbounds nuw i32, ptr %15, i64 %30
  store <4 x i32> %35, ptr %36, align 16, !tbaa !5
  %37 = add nuw i64 %30, 4
  %38 = icmp eq i64 %37, %28
  br i1 %38, label %39, label %29, !llvm.loop !9

39:                                               ; preds = %29
  %40 = icmp eq i64 %28, %20
  br i1 %40, label %66, label %41

41:                                               ; preds = %23, %8, %39
  %42 = phi i64 [ 0, %23 ], [ 0, %8 ], [ %28, %39 ]
  %43 = and i64 %20, 1
  %44 = icmp eq i64 %43, 0
  br i1 %44, label %53, label %45

45:                                               ; preds = %41
  %46 = getelementptr inbounds nuw i32, ptr %12, i64 %42
  %47 = load i32, ptr %46, align 16, !tbaa !5
  %48 = getelementptr i32, ptr %21, i64 %42
  %49 = load i32, ptr %48, align 4, !tbaa !5
  %50 = tail call noundef i32 @llvm.smin.i32(i32 %47, i32 %49)
  %51 = getelementptr inbounds nuw i32, ptr %15, i64 %42
  store i32 %50, ptr %51, align 16, !tbaa !5
  %52 = or disjoint i64 %42, 1
  br label %53

53:                                               ; preds = %45, %41
  %54 = phi i64 [ %42, %41 ], [ %52, %45 ]
  %55 = add nsw i64 %20, -1
  %56 = icmp eq i64 %42, %55
  br i1 %56, label %66, label %71

57:                                               ; preds = %4, %2
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 4), align 4, !tbaa !5
  br label %99

58:                                               ; preds = %66
  store i32 0, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 4), align 4, !tbaa !5
  %59 = add nuw i32 %1, 1
  %60 = zext i32 %59 to i64
  %61 = and i64 %60, 1
  %62 = icmp eq i32 %59, 3
  br i1 %62, label %90, label %63

63:                                               ; preds = %58
  %64 = and i64 %60, 4294967294
  %65 = add nsw i64 %64, -4
  br label %100

66:                                               ; preds = %53, %71, %39
  %67 = add nuw nsw i64 %9, 1
  %68 = trunc nuw nsw i64 %9 to i32
  %69 = shl nuw i32 2, %68
  %70 = icmp sgt i32 %69, %1
  br i1 %70, label %58, label %8, !llvm.loop !13

71:                                               ; preds = %53, %71
  %72 = phi i64 [ %86, %71 ], [ %54, %53 ]
  %73 = getelementptr inbounds nuw i32, ptr %12, i64 %72
  %74 = load i32, ptr %73, align 4, !tbaa !5
  %75 = getelementptr i32, ptr %21, i64 %72
  %76 = load i32, ptr %75, align 4, !tbaa !5
  %77 = tail call noundef i32 @llvm.smin.i32(i32 %74, i32 %76)
  %78 = getelementptr inbounds nuw i32, ptr %15, i64 %72
  store i32 %77, ptr %78, align 4, !tbaa !5
  %79 = add nuw nsw i64 %72, 1
  %80 = getelementptr inbounds nuw i32, ptr %12, i64 %79
  %81 = load i32, ptr %80, align 4, !tbaa !5
  %82 = getelementptr i32, ptr %21, i64 %79
  %83 = load i32, ptr %82, align 4, !tbaa !5
  %84 = tail call noundef i32 @llvm.smin.i32(i32 %81, i32 %83)
  %85 = getelementptr inbounds nuw i32, ptr %15, i64 %79
  store i32 %84, ptr %85, align 4, !tbaa !5
  %86 = add nuw nsw i64 %72, 2
  %87 = icmp eq i64 %86, %20
  br i1 %87, label %66, label %71, !llvm.loop !14

88:                                               ; preds = %100
  %89 = icmp eq i64 %61, 0
  br i1 %89, label %99, label %90

90:                                               ; preds = %88, %58
  %91 = phi i64 [ 2, %58 ], [ %116, %88 ]
  %92 = icmp ne i64 %61, 0
  tail call void @llvm.assume(i1 %92)
  %93 = lshr i64 %91, 1
  %94 = and i64 %93, 2147483647
  %95 = getelementptr inbounds nuw i32, ptr @lg, i64 %94
  %96 = load i32, ptr %95, align 4, !tbaa !5
  %97 = add nsw i32 %96, 1
  %98 = getelementptr inbounds nuw i32, ptr @lg, i64 %91
  store i32 %97, ptr %98, align 4, !tbaa !5
  br label %99

99:                                               ; preds = %90, %88, %57
  ret void

100:                                              ; preds = %100, %63
  %101 = phi i64 [ 2, %63 ], [ %116, %100 ]
  %102 = phi i64 [ 0, %63 ], [ %117, %100 ]
  %103 = lshr exact i64 %101, 1
  %104 = and i64 %103, 2147483647
  %105 = getelementptr inbounds nuw i32, ptr @lg, i64 %104
  %106 = load i32, ptr %105, align 4, !tbaa !5
  %107 = add nsw i32 %106, 1
  %108 = getelementptr inbounds nuw i32, ptr @lg, i64 %101
  store i32 %107, ptr %108, align 8, !tbaa !5
  %109 = lshr exact i64 %101, 1
  %110 = and i64 %109, 2147483647
  %111 = getelementptr inbounds nuw i32, ptr @lg, i64 %110
  %112 = load i32, ptr %111, align 4, !tbaa !5
  %113 = add nsw i32 %112, 1
  %114 = getelementptr inbounds nuw i32, ptr @lg, i64 %101
  %115 = getelementptr inbounds nuw i8, ptr %114, i64 4
  store i32 %113, ptr %115, align 4, !tbaa !5
  %116 = add nuw nsw i64 %101, 2
  %117 = add i64 %102, 2
  %118 = icmp eq i64 %102, %65
  br i1 %118, label %88, label %100, !llvm.loop !15
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local noundef i32 @sparse_query(i32 noundef %0, i32 noundef %1) local_unnamed_addr #1 {
  %3 = sub nsw i32 %1, %0
  %4 = sext i32 %3 to i64
  %5 = getelementptr i32, ptr @lg, i64 %4
  %6 = getelementptr i8, ptr %5, i64 4
  %7 = load i32, ptr %6, align 4, !tbaa !5
  %8 = sext i32 %7 to i64
  %9 = getelementptr inbounds [100000 x i32], ptr @st, i64 %8
  %10 = sext i32 %0 to i64
  %11 = getelementptr inbounds i32, ptr %9, i64 %10
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = shl nsw i32 -1, %7
  %14 = add i32 %13, %1
  %15 = sext i32 %14 to i64
  %16 = getelementptr i32, ptr %9, i64 %15
  %17 = getelementptr i8, ptr %16, i64 4
  %18 = load i32, ptr %17, align 4, !tbaa !5
  %19 = tail call noundef i32 @llvm.smin.i32(i32 %12, i32 %18)
  ret i32 %19
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local noundef range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  tail call void @llvm.memcpy.p0.p0.i64(ptr noundef nonnull align 16 dereferenceable(28) @st, ptr noundef nonnull readonly align 16 dereferenceable(28) @__const.main.a, i64 28, i1 false), !tbaa !5
  store <4 x i32> <i32 2, i32 2, i32 4, i32 1>, ptr getelementptr inbounds nuw (i8, ptr @st, i64 400000), align 16, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @st, i64 400016), align 16, !tbaa !5
  store i32 3, ptr getelementptr inbounds nuw (i8, ptr @st, i64 400020), align 4, !tbaa !5
  store <4 x i32> <i32 2, i32 1, i32 1, i32 1>, ptr getelementptr inbounds nuw (i8, ptr @st, i64 800000), align 16, !tbaa !5
  store <4 x i32> <i32 0, i32 1, i32 1, i32 2>, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 4), align 4, !tbaa !5
  store i32 2, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 20), align 4, !tbaa !5
  store i32 2, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 24), align 8, !tbaa !5
  store i32 2, ptr getelementptr inbounds nuw (i8, ptr @lg, i64 28), align 4, !tbaa !5
  %1 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  ret i32 0
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias writeonly captures(none), ptr noalias readonly captures(none), i64, i1 immarg) #3

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #4

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #4

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare <4 x i32> @llvm.smin.v4i32(<4 x i32>, <4 x i32>) #4

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #6

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(readwrite, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #4 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #5 = { nofree nounwind }
attributes #6 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10, !11, !12}
!10 = !{!"llvm.loop.mustprogress"}
!11 = !{!"llvm.loop.isvectorized", i32 1}
!12 = !{!"llvm.loop.unroll.runtime.disable"}
!13 = distinct !{!13, !10}
!14 = distinct !{!14, !10, !11}
!15 = distinct !{!15, !10}
